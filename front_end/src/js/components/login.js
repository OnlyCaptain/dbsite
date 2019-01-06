import React, { Component} from 'react';
import {
  Form, Icon, Input, Button, message
} from 'antd';
import '../../css/Form.css'
import logo from '../../images/login.png';
import {stringify} from 'qs';
import { Link } from 'react-router-dom'

class LoginPage extends Component{

  constructor(){
    super();
    this.state={
      UserName: null,
      Password: null,
    };
  }

  handleGetUserName = (event)=>{
    this.setState({
      UserName : event.target.value,
    });
  };

  handleGetPassword = (event)=>{
    this.setState({
      Password : event.target.value,
    });
  };

  handleLogin = () => {
    const content = {UserName:this.state.UserName,
      Password:this.state.Password}
      
    fetch('http://182.254.231.51:8000/api/login/',{
      method:"POST",
      headers: {
        'Content-Type':'application/x-www-form-urlencoded'
      },
      body:stringify(content)
    }).then(response => {
      if(response.status == 200){
        // 登录成功,跳转
        message.success("登录成功!正在跳转,请稍等...");
        return response.json();
      }
      else if(response.status == 404){
        // 用户名不存在
        message.error("用户名不存在, 请重新输入!");
      }
      else if(response.status == 403){
        // 密码错误
        message.error("密码错误, 请重新输入!");
      }
    }).then(data => {
      let path = '/User/'+String(data);
      this.props.history.push({ pathname: path, state:{data}});
    });
  }

  render() {
    const { getFieldDecorator } = this.props.form;
    return (
      <div className="background-image">
        <span style={{display: 'inline-block',paddingTop: '10%',paddingLeft: '38%'}}>
        <img src={logo}/>
        <Form className="login-form">
          <Form.Item>
            {getFieldDecorator('userName', {
              rules: [{ required: true, message: '请输入用户名!' }],
            })(
              <Input 
                prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />} 
                placeholder="账号"
                onChange={this.handleGetUserName}
              />
            )}
          </Form.Item>
          <Form.Item>
            {getFieldDecorator('Password', {
              rules: [{ required: true, message: '请输入密码!' }],
            })(
              <Input
                prefix={<Icon type="lock"
                style={{ color: 'rgba(0,0,0,.25)' }} />}
                type="password" 
                placeholder="密码"
                onChange={this.handleGetPassword}
              />
            )}
          </Form.Item>
          <Form.Item>
            <Button type="primary" className="login-form-button" onClick={this.handleLogin}>
              登录
            </Button>
            还没有账号? <Link to='/register'>马上注册!</Link>
          </Form.Item>
        </Form>
        </span>
      </div>
    );
  }
}

const WrappedNormalLoginForm = Form.create()(LoginPage);
export default WrappedNormalLoginForm;