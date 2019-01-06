import { Layout, Menu, Button, Icon, message, Modal, Input } from 'antd';
const { TextArea } = Input;
import React, { Component } from 'react';
import 'antd/dist/antd.css';
import logo from '../../images/logo.png';
import '../../css/Navi.css'
const { Header, Footer, Sider } = Layout;
import {withRouter} from 'react-router';
import Questions from './QuestionList'
import {stringify} from 'qs';

class MainPage extends Component {
  constructor(props){
    super(props);
    this.state = {
      collapsed: true,
      mode: 'inline',
      hasLogined: true,
      modal1Visible: false,
      UserId: this.props.location.state.data,
      postQuesTitle: "",
      postQuesDescrip: "",
    };
  }

  // 跳转到登录页面
  Login(){
    location.href='/login';
  }

  // 退出登录注销账号
  Logout(){
    this.setState({
      hasLogined: false,
    });
    message.success("注销成功!");
  }
  
  // 提出问题的Modal
  showModal(){
    this.setState({
      modal1Visible: true,
    });
  }

  hideModal(){
    this.setState({
      modal1Visible: false,
      postQuesTitle: "",
      postQuesDescrip: "",
    })
  }
  
  // 处理侧边栏的点击
  handleClick(e){
    switch(e.key){
      case "1":
        // 提出问题
        this.showModal();
      case "2":
        // 个人信息

      case "3":
        // 我的问题
    }
  }

  postQuestion(){

    if(this.state.postQuesTitle ==  ""){
      message.error("标题为空, 请重新输入!");
      return;
    }
    const content = {Title:this.state.postQuesTitle, QuestionOwner: this.state.UserId,
      Description:this.state.postQuesDescrip};

    fetch('http://182.254.231.51:8000/api/questions/',{
      method:"POST",
      headers: {
        'Content-Type':'application/x-www-form-urlencoded'
      },
      body:stringify(content)
    }).then(response => {
      console.log(response);
      if(response.status == 201){
        // 提出问题成功,跳转
        message.success("提问成功!");
        this.hideModal();
      }
    });
  }

  toggle(){
    this.setState({
      collapsed: !this.state.collapsed,
    });
  }

  onChangeTitle=(e)=>{
    this.setState({postQuesTitle: e.target.value});
  }

  onChangeDescription=(e)=>{
    this.setState({postQuesDescrip: e.target.value});
  }

  render() {
    return (
      <Layout>
        <Modal
          title="提出新问题"
          visible={this.state.modal1Visible}
          centered
          onOk={()=>this.postQuestion()}
          onCancel={()=>this.hideModal()}
        >
          <div>
            <TextArea placeholder="问题描述" autosize="true" onChange={this.onChangeTitle} value={this.state.postQuesTitle}/>
          <div style={{ margin: '24px 0' }} />
          <TextArea placeholder="问题详细" autosize={{ minRows: 4, maxRows: 20 }} onChange={this.onChangeDescription} value={this.state.postQuesDescrip} />
          </div>
        </Modal>
        <Sider
          trigger={null}
          collapsible
          collapsed={this.state.collapsed}
        >
          <Menu theme="dark" mode="inline" onClick={(e)=>this.handleClick(e)}>
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
              {this.state.hasLogined ? <Button type="primary" onClick={()=>this.Logout()} >注销</Button> : <Button type="primary" onClick={this.Login}>登录/注册</Button>}
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

export default withRouter(MainPage);