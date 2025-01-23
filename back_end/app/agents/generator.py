##包装openai的方法，将大模型返回的内容return出去
# 参考 autoCircos\back_end\test.py 文件

import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

# 从 .env 文件中获取密钥和 API 基础地址
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key=api_key,  # 从环境变量中加载 API 密钥
    base_url=base_url,  # 从环境变量中加载自定义 API 地址
)

# 读取当前目录下的文件
# file_path = "circosjsRM.md"
file_path = os.path.join(os.path.dirname(__file__), "circosjsRM.md")

with open(file_path, "r", encoding="utf-8") as file:
    markdown_text = file.read()


code_template = """
<script setup>
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';
import Circos from 'circos';
import { readFile } from '@/utils/server'; // 引入封装的 readFile API 调用
import { delete_overflow, reduceData, reduceData_Position, transform_startend_position, gieStainColor } from './utils_circos.js';
onMounted(async () => {
  try {
    //获取参考基因组文件
    let hg19 = await d3.json('/data/hg19.json')
    let cytobands = await d3.csv('/data/cytobands.csv');

    //设置画布
    let chartWidth = document.getElementById('chart').clientWidth;
    let width = chartWidth;
    let innerRadius = chartWidth/2-100;
    let outerRadius = chartWidth/2-100+50;

    //初始化circos
    const circos = new Circos({
      container: `#chart`,
      width: width,
      height: width,
    });
    circos.layout(
      hg19,
      {
        innerRadius: innerRadius,
        outerRadius: outerRadius,
        labels: {
          display: true,
          radialOffset: 60,
          color: "black",
          size: 10
        },
        ticks: {
          display: true,
          color: 'grey',
          labels: false,
          labelSuffix: 'Mb',//百万级别
          labelDenominator: 5000000,
          spacing: 5000000,
          labelSize: 5,
          labelColor: 'grey',

        },
      }
    );
    //绘制参考基因组染色体
    let highlightData = cytobands.map(function (d) {
      return {
        block_id: d.id,
        start: parseInt(d.start),
        end: parseInt(d.end),
        gieStain: d.gieStain
      }
    })

    let highlightConfig = {
      innerRadius: innerRadius,
      outerRadius: outerRadius,
      opacity: .7,
      color: function (d) {
        return gieStainColor[d.gieStain]
      }
    }

    circos.highlight('highlight', highlightData, highlightConfig)
    //The above are some basic configurations, 
    //code generated by llm should be written below


    circos.render();
  } catch (err) {
    console.error('Error fetching or processing data:', err);
  }
});
</script>

<!-- The following code should not be changed -->
<template>
  <div id="chart"></div>
</template>

<style scoped>
#chart {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%; 
  height: 100%;
}
</style>

"""
# 每次读取前端的代码作为基础，前端发送文件内容

# 获取当前文件所在路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 定义 demo1.vue 文件的相对路径
vue_file_path = os.path.join(current_dir, '../../..', 'front_end', 'autocc', 'src', 'components', 'Center', 'demo1.vue')

# 确保文件路径正确
vue_file_path = os.path.abspath(vue_file_path)

# 读取文件内容
try:
    with open(vue_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        print(file_content)  # 或者返回 file_content 以供后续使用
except FileNotFoundError:
    print(f"Error: {vue_file_path} not found.")
except Exception as e:
    print(f"Error reading file: {str(e)}")


# 调用 API 的方法
def use_generator(query,queryInfo,basecode,model="gpt-4o"):

    file_name = queryInfo["file_name"]
    chart_type = queryInfo["chart_type"]
    query_type = queryInfo["query_type"]
    track_id = queryInfo["track_id"]
    

    if file_name != "":
        # 读取根目录下data文件夹中id_001下的file_name文件
        file_path = f"data/id_001/{file_name}"
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.readline()
        file_columns = file_content.strip().split(",")
        prompt = f"""
        Please use the circosjs library to create a chart based on the user's request: {query}.
        I will provide you with documentation on how to use this library, and please write the code according to the instructions in the documentation.
        Additionally, I will give you an existing code template. Please add new code to this template in order to implement the functionality or chart described in {query}.
        The file name used in this generated code is: {file_name}, and the column name of this file is: {file_columns}
        the documentation is:
        {markdown_text}

        the existing code template is:
        {basecode}
        """

    try:
        # 调用 Chat Completion 接口
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{prompt} \n and the user query is:{query}"},
            ],
            model=model,
            
            temperature=0.7,
        )

        # 返回生成的内容
        reply = chat_completion.choices[0].message.content
        # 将生成的内容写入当前文件夹下的demo1.vue文件
        with open("demo1.vue", "w", encoding="utf-8") as file:
            file.write(reply)
        return 200
    except Exception as e:
        print(f"调用 OpenAI API 时出错：{e}")
        return 500