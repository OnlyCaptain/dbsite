import {
    Form, Icon, Input, Button, Checkbox, Modal,
  } from 'antd';
import React, { Component } from 'react';
import 'antd/dist/antd.css';
import '../../css/Form.css';

// const 
  
export default class LoginForm extends React.Component {
  constructor(){
    super();
    this.state={
      hasLogined: false,
      visible: false,
    };
  }

  setModalVisible(flag){
    this.setState({visible: flag})
  }

  selectBtn(){
    if(this.state.hasLogined){
      return(<Button type="primary">退出登录</Button>);
    }
    else{
      return(<Button type="primary" onClick={() => this.setModalVisible(true)}>登录/注册</Button>);
    }
  }

  render() {
    return (
      <span style={{color:'#fff', paddingLeft:'65%'}}>
        {this.selectBtn()}
        <Modal
          title="Basic Modal"
          visible={this.state.visible}
          footer={null}
        >
          <p>testing</p>
        </Modal>
      </span> 
    );
  }
}