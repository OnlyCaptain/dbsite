import { Layout, Menu, Button, Icon, Modal } from 'antd';
import React, { Component } from 'react';
import 'antd/dist/antd.css';
import logo from '../../images/logo.png';
import '../../css/Navi.css'
const { Header, Content, Footer, Sider } = Layout;

import Questions from './questions'

export default class MainPage extends Component {
  constructor(){
    super();
    this.state = {
      collapsed: true,
      mode: 'inline',
      hasLogined: false,
      modal1Visable: false,
    };
  }
  
  // 处理侧边栏的点击
  handleClick(e){
    switch(e){
      case "1":
        // 提出问题
      case "2":
        // 个人信息

      case "3":
        // 我的问题
    }
  }

  toggle(){
    this.setState({
      collapsed: !this.state.collapsed,
    });
  }

  render() {
    return (
      <Layout>
        <Sider
          trigger={null}
          collapsible
          collapsed={this.state.collapsed}
        >
          <Menu theme="dark" mode="inline" onClick={this.handleClick.bind(this)}>
            <Menu.Item key="1">
              <Icon type="edit" />
              <span className="nav-text">提出问题</span>
            </Menu.Item>
            <Menu.Item key="2">
              <Icon type="user" />
              <span className="nav-text">个人信息</span>
            </Menu.Item>
            <Menu.Item key="3">
              <Icon type="bars" />
              <span className="nav-text">我的问题</span>
            </Menu.Item>
          </Menu>
        </Sider>

        <Layout>
          <Header style={{ background: '#000', padding: 0 }}>
            <span style={{color:'#fff', paddingLeft:'2%', fontSize:'1.4em'}}>
              <Icon
                className="trigger"
                type={this.state.collapsed ? 'menu-unfold' : 'menu-fold'}
                onClick={() => this.toggle()}
                style={{cursor: 'pointer'}}
              />
            </span>

            <span className="welcome" style={{color:'#fff', paddingLeft:'2%', fontSize:'1.4em'}}>Welcome to Quaaaaro!</span>
            
            <span style={{color:'#fff', paddingLeft:'65%'}}>
              <Button type="primary">退出登录</Button>
            </span>

            <span style={{color:'#fff', float:'right', paddingRight:'1%'}}>
              <img src={logo} className="App-logo" alt="logo" />
            </span>
          </Header>

          <Questions/>

          <Footer style={{ textAlign: 'center' }}>
            Quaro ©2018 Created by JanHoChoi
          </Footer>
        </Layout>
      </Layout>
    );
  };
}