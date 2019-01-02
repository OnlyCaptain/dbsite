import { Layout, Menu, Breadcrumb, Icon } from 'antd';
import React, { Component } from 'react';
import 'antd/dist/antd.css';


export default class Questions extends Component {
  constructor(){
    super();
  }
  render() {
    return (
      <Layout style={{ margin: '0 16px' }}>
        <Breadcrumb style={{ margin: '12px 0' }}>
          <Breadcrumb.Item href="">
            <Icon type="home" />
            <span>主页</span>
          </Breadcrumb.Item>
          <Breadcrumb.Item href="">
            <Icon type="heart" />
            <span>关注</span>
          </Breadcrumb.Item>
        </Breadcrumb>
        <div style={{ padding: 24, background: '#fff', minHeight: 780 }}>
          占坑
        </div>
      </Layout>
    );
  };
}