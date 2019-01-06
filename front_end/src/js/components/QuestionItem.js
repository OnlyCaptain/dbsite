import React, { Component } from 'react';
import { Button, Layout } from 'antd';

export default class QuestionItem extends Component {

  constructor(props){
    super(props);
    this.state = {
      vote: 0,
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

  handleClick(){
    this.props.onSelectQuestion(this.props.id, this.props.title, this.props.description);
  }

  render(){
    return(
      <Layout style={{ margin: '5px' }}>
      <div style={{padding: 24, background: '#fff'}}>
        <div>
          <h3 className="media-heading">{this.props.title}</h3>
          <p>{this.props.description}...</p>
        </div>
        <div>
          <Button icon="up" onClick={()=>this.voteUp()}>
	          <span className="vote-count">{this.state.vote}</span>
          </Button>
          <span>&nbsp;&nbsp;</span>
          <Button icon="down" onClick={()=>this.voteDown()}>
          </Button>
          <span style={{paddingLeft:"85%"}}>
            <Button type="primary" onClick={()=>this.handleClick()}>查看问题详细</Button>
          </span>
	      </div>
      </div>
      </Layout>
    );
  };
}