# README

## 注意

尽量不要修改以下几个文件：

1. ./webpack/webpack.config.js
2. package.json(package-lock.json)
3. .babelrc

## 怎么运行

```
npm run dev
```

缺什么环境配什么。（可能需要安装node.js，网上找博客随便配）

## 配环境

打开package.json

```
"dependencies": {
    "antd": "^3.11.6",
    "react": "^16.7.0",
    "react-dom": "^16.7.0",
    "react-responsive": "^6.0.1",
    "react-router": "^4.3.1",
    "yarn": "^1.12.3"
  },
  "devDependencies": {
    "@babel/core": "^7.2.2",
    "@babel/preset-env": "^7.2.3",
    "@babel/preset-react": "^7.0.0",
    "babel-loader": "^8.0.4",
    "babel-plugin-transform-class-properties": "^6.24.1",
    "css-loader": "^2.1.0",
    "style-loader": "^0.23.1",
    "url-loader": "^1.1.2",
    "webpack": "^4.28.3",
    "webpack-cli": "^3.1.2",
    "webpack-dev-server": "^3.1.14"
  },
```

对于dependencies:

```
npm install --save antd
npm install --save react
...
也可以一次性npm install --save antd react react-dom...
```

对于devDependencies:

```
npm install --save-dev @babel/core...
```

## 入口

package.json的

```
...
"main": "./src/js/index.js",
...
```

webpack会把index.js编译成bundle.js。

用户访问的页面是index.html（里面用到了bundle.js的代码）。