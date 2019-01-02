# README

## 怎么运行

```
npm run dev
```

缺什么环境配什么。

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

