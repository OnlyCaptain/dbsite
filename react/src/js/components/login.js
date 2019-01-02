import React, { Component} from 'react';
import {
  Form, Icon, Input, Button, Checkbox,
} from 'antd';
import '../../css/Form.css'
import logo from '../../images/login.png';

var serverUrl = "http://182.254.231.51:8000/";


class LoginPage extends Component{

  constructor(){
    super();
    this.state={
      account: null,
      password: null,
    };
  }

  handleGetAccount = (event)=>{
    this.setState({
      account : event.target.value,
    })
  };

  handleGetPassword = (event)=>{
    this.setState({
      password : event.target.value,
    })
  };

  handleLogin = ()=> {
    console.log(this.state.account,'------用户名');
    console.log(this.state.password,'------密码');
    // 向服务器确认是否可以登陆

    
    // fetch(serverUrl)
    //   .then(function(response) {
    //     return response.json();
    //   })
    //   .then(function(myJson) {
    //     console.log(myJson);
    //   });

  }

  render() {
    const { getFieldDecorator } = this.props.form;
    return (
      <span>
      <img src={logo}/>
      <Form className="login-form">
        <Form.Item>
          {getFieldDecorator('userName', {
            rules: [{ required: true, message: 'Please input your username!' }],
          })(
            <Input 
              prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />} 
              placeholder="账号"
              onChange={this.handleGetAccount}
              value={this.state.account}
            />
          )}
        </Form.Item>
        <Form.Item>
          {getFieldDecorator('password', {
            rules: [{ required: true, message: 'Please input your Password!' }],
          })(
            <Input
              prefix={<Icon type="lock"
              style={{ color: 'rgba(0,0,0,.25)' }} />}
              type="password" 
              placeholder="密码"
              onChange={this.handleGetPassword}
              value={this.state.password}
            />
          )}
        </Form.Item>
        <Form.Item>
          {getFieldDecorator('remember', {
            valuePropName: 'checked',
            initialValue: true,
          })(
            <Checkbox>记住账号</Checkbox>
          )}
          <a className="login-form-forgot" href="">忘记密码</a>
          <Button type="primary" className="login-form-button" onClick={this.handleLogin}>
            登录
          </Button>
          还没有账号? <a href="http://www.baidu.com">马上注册!</a>
        </Form.Item>
      </Form>
      </span>
    );
  }
}

const WrappedNormalLoginForm = Form.create()(LoginPage);
export default WrappedNormalLoginForm;