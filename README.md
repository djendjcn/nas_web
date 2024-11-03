# nas_web

# 项目构建步骤

## build前端
在nas_client目录下执行
```
npm run build
```
会生成新的dist目录，并自动保存到nas_server/static目录下
## build后端
在nas_server目录下执行
```
pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "templates/static;templates/static" app.py

```

