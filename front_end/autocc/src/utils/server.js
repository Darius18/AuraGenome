// server.js
import axios from './axios';

// 调用后端 `/read-file` 接口的方法
export const readFile = async (filepath) => {
    try {
        const response = await axios.post('/read-file', { filepath });
        // 返回文件内容或下载链接
        return response.data;
    } catch (error) {
        // 捕获错误并返回错误信息
        console.error('Error in readFile API:', error);
        throw error;
    }
};
