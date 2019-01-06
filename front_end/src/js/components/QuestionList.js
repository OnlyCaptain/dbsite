import { Layout , Button, message, Modal, Input} from 'antd';
const { TextArea } = Input;
import React, { Component } from 'react';
import 'antd/dist/antd.css';
import QuestionItem from './QuestionItem';
import AnswerItem from './AnswerItem';

export default class Questions extends Component {

  constructor(){
    super();
    this.state={
      loadList: false,
      questions: null,
      modalVisible: false,
      loadQues: false,
      selectId: 0,
      answers: null,
      selectTitle: "",
      selectDescription: "",
    }
    this.handleSelectQuestion = this.handleSelectQuestion.bind(this);
  }

  //耗时操作放在这里面
  componentDidMount(){
    this.getQuestionLists();
    // this.getQuestionDetail();
  }

  getQuestionLists(){
    fetch('http://182.254.231.51:8000/api/questions/',{
      method:"GET"
    }).then(response => {
      return response.json();
    }).then(data => {
      this.setState({
        loadList: true,
        questions: data
      })
    });
  };

  handleSelectQuestion(QuesId, QuesTitle, QuesDescrip){
    let url = "http://182.254.231.51:8000/api/answers/" + String(QuesId);
    console.log(url);
    fetch(url,{
      method:"GET"
    }).then(response => {
      return response.json();
    }).then(data => {
      this.setState({
        answers: data,
        loadQues: true,
        selectId: QuesId,
        selectTitle: QuesTitle,
        selectDescription: QuesDescrip,
      });
    });
  }

  handleFixQuestion(){
    message.error("你不是问题的提出者,无法修改该回答!");
  }

  postAnswer(){
    this.setState({
      modalVisible: true,
    });
  }

  test(){
    this.setState({
      modalVisible: false,
    });
    message.success("回答问题成功!");
  }

  render() {
    if(this.state.loadList && this.state.selectId == 0){
      const QuestionComp = this.state.questions.map(
        (item) => 
        <QuestionItem key={item.id} 
          id={item.id} 
          title={item.Title} 
          description={item.Description} 
          time={item.date_added}
          onSelectQuestion={this.handleSelectQuestion}
        />
      );
      return (
        <Layout style={{ margin: '30px 16px'}}>
          {QuestionComp}
        </Layout>
      );
    }
    else if(this.state.loadQues && this.state.selectId > 0){

      const AnswerComp = this.state.answers.map(
        (item) =>
        <AnswerItem key={item.id}
        Owner={item.AnswerOwner}
        AnswerWords={item.AnswerWords}
        />
      );

      return (
        <Layout style={{ margin: '30px 16px' }}>
        <Modal
          title="回答该问题"
          visible={this.state.modalVisible}
          centered
          onOk={()=>this.test()}
        >
          <div>
            <TextArea placeholder="回答内容" autosize={{ minRows: 4, maxRows: 20 }} />
          </div>
        </Modal>
          <div style={{ padding: 24, background: '#fff'}}>
            <h2>{this.state.selectTitle}</h2>
            <p>{this.state.selectDescription}</p>
            <span>
              <Button type="primary">关注问题</Button>
              <span>&nbsp;&nbsp;</span>
              <Button icon="edit" onClick={()=>this.postAnswer()}>写回答</Button>
              <span>&nbsp;&nbsp;</span>
              <Button type="danger" onClick={()=>this.handleFixQuestion()}>
                修改该问题
              </Button>
            </span>
          </div>
          <div>
            {AnswerComp}
          </div>
        </Layout>
      );
    }
    else{
      return (
        <Layout style={{ margin: '30px 16px' }}>
          <div style={{ padding: 24, background: '#fff', minHeight: 780 }}>
            Loading...
          </div>
        </Layout>
      );
    }
  };
}