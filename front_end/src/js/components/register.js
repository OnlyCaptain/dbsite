import React, { Component} from 'react';
import {
  Form, Icon, Input, Button, message
} from 'antd';
import '../../css/Form.css'
import logo from '../../images/login.png';
import {stringify} from 'qs';

class RegisterPage extends Component{

  constructor(){
    super();
    this.state={
      UserName: null,
      Password: null,
      Confirm: null,
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

  handleGetConfirm = (event)=>{
    this.setState({
      Confirm : event.target.value,
    });
  };

  handleRegister = () => {

    console.log(this.state.UserName,'------用户名');
    console.log(this.state.Password,'------密码');
    console.log(this.state.Confirm,'------二次密码');
    // 向服务器确认是否可以登陆

    if(this.state.Password != this.state.Confirm){
      message.error("两次密码不相同, 请重新输入!");
      return;
    }

    console.log('尝试发包');

    const content = {UserName:this.state.UserName,
      Password:this.state.Password}

    fetch('http://182.254.231.51:8000/api/register/',{
      method:"POST",
      headers: {
        'Content-Type':'application/x-www-form-urlencoded'
      },
      body:stringify(content)
    }).then(response => {
      console.log(response);
      if(response.status == 200){
        // 注册成功,跳转
        message.success("注册成功!正在跳转,请稍等...");
        let path = '/User/'+String(this.state.UserName);
        let UserName = this.state.UserName;
        this.props.history.push({ pathname: path, state:{UserName} });
      }
      else if(response.status == 403){
        message.error("用户名已存在, 请重新输入!");
      }
    });

  }

  render() {
    const { getFieldDecorator } = this.props.form;

    const formItemLayout = {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 8 },
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 16 },
      },
    };

    const tailFormItemLayout = {
      wrapperCol: {
        xs: {
          span: 24,
          offset: 0,
        },
        sm: {
          span: 16,
          offset: 8,
        },
      },
    };

    return (
      <div className="background-image">
        <span style={{display: 'inline-block',paddingTop: '10%',paddingLeft: '38%'}}>
        <img src={logo}/>
          <Form>
            <Form.Item
              {...formItemLayout}
              label="用户名"
            >
            {getFieldDecorator('UserName', {
              rules: [{
                type: 'string',
              }, {
                required: true, message: '请输入用户名!',
              }],
            })(
              <Input onChange={this.handleGetUserName}/>
            )}
            </Form.Item>

            <Form.Item
              {...formItemLayout}
              label="密码"
            >
            {getFieldDecorator('Password', {
              rules: [{
                required: true, message: '请输入密码!',
              }],
            })(
              <Input type="password" onChange={this.handleGetPassword}/>
            )}
            </Form.Item>
            <Form.Item
              {...formItemLayout}
              label="再次输入密码"
            >
              {getFieldDecorator('confirm', {
                rules: [{
                  required: true, message: 'Please confirm your password!',
                }],
              })(
                <Input type="password" onChange={this.handleGetConfirm} />
              )}
            </Form.Item>
            <Form.Item {...tailFormItemLayout}>
              <Button type="primary" onClick={this.handleRegister}>注册</Button>
            </Form.Item>
          </Form>
        </span>
      </div>
    );
  }
}

const WrappedNormalRegisterForm = Form.create()(RegisterPage);
export default WrappedNormalRegisterForm;