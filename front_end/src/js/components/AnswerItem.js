import React, { Component } from 'react';
import { Button, Layout, message, Modal } from 'antd';

export default class QuestionItem extends Component {

  constructor(props){
    super(props);
    this.state = {
      vote: 0,
      modalVisible: false,
    };
  }
  voteUp(){
    this.setState({
      vote: this.state.vote+1,
    })
  }
  voteDown(){
    this.setState({
      vote: this.state.vote-1,
    })
  }

  postAnswer(){
    this.setState({
      modalVisible: true
    });
  }

  handleFixAnswer(){
    message.error("你不是回答者,无法修改该回答!");
  }

  render(){
    return(
      <Layout style={{ margin: '5px' }}>
      <div style={{padding: 24, background: '#fff'}}>
        <h3>回答者 id:{this.props.Owner}</h3>
        <div>
          <p>{this.props.AnswerWords}</p>
        </div>
        <Button icon="up" onClick={()=>this.voteUp()}>
	        <span className="vote-count">{this.state.vote}</span>
        </Button>
        <span>&nbsp;&nbsp;</span>
        <Button icon="down" onClick={()=>this.voteDown()}>
        </Button>
        <span style={{paddingLeft:"85%"}}>
        <Button type="danger" onClick={()=>this.handleFixAnswer()}>
          修改该回答
        </Button>
        </span>

      </div>
      </Layout>
    );
  };
}