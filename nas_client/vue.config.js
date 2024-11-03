const { defineConfig } = require('@vue/cli-service')
const path = require('path');
module.exports = defineConfig({
  publicPath: './', // 使用相对路径
  transpileDependencies: true,
  outputDir: path.resolve(__dirname, '../nas_server/templates/static'), // 设置构建输出目录
})
