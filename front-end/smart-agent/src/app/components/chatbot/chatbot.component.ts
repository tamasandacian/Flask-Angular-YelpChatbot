import { Component, OnInit } from '@angular/core';
import { ChatbotService } from 'src/app/services/chatbot.service';
import { Subject } from 'rxjs';

export class Chat {
  message: any;
  isMe: boolean;
  type: string;

  constructor(message: string, isMe: boolean, type: string) { }
}
@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {

  startPage: Number;
  paginationLimit: Number;

  conversation = new Subject<Chat[]>();
  chats: Chat[] = [];
  message: string;

  constructor(private chatbotService: ChatbotService) {
    this.startPage = 0;
    this.paginationLimit = 3;

  }

  ngOnInit() {
    // Display Welcome message in the Smart Agent Portal
    let userMessage_default = { message: '', isMe: false, type: '' }
    let chatbotMessage_default = {
      message:
        [{
          "_type": "welcome",
          "answer": "Welcome to our search platform. I’m YelpBot. You can ask me anything related to restaurants and different food types ..."
        }],

      isMe: false,
      type: 'bot'
    }

    setTimeout(() => {
      this.chats = [userMessage_default, chatbotMessage_default]
    }, 1500);

    this.conversation.subscribe((val) => {
      this.chats = this.chats.concat(val);
    });

  }


  sendMessage() {
    this.getBotAnswer(this.message);
    this.message = '';
  }

  getBotAnswer(msg: string) {

    // Send User message
    let userMessage = { message: msg, isMe: true, type: 'user' }
    this.conversation.next([userMessage]);

    let botMessage: any;
    this.chatbotService.send_message(this.message).subscribe(data => {

      // If message found send location data to MapComponent
      this.chatbotService.send_data_to_map_component(data);


      // Send Bot message
      botMessage = { message: data, isMe: false, type: 'bot' };
      this.conversation.next([botMessage]);

      // Set timer to display bot message (optional)
      /*
      setTimeout(() => {
        this.conversation.next([botMessage]);
      }, 500);
      */

    });

  }

  showMore() {
    this.paginationLimit = Number(this.paginationLimit) + 3;
  }
  showLess() {
    this.paginationLimit = Number(this.paginationLimit) - 3;
  }


}