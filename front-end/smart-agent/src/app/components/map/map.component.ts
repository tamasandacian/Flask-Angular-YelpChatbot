import { Component, OnInit } from '@angular/core';
import { ChatbotService } from 'src/app/services/chatbot.service';
import { TouchSequence } from 'selenium-webdriver';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  propertyList: any[] = [];
  propertyObj: any;
  public latitude: number;
  public longitude: number;
  public zoom: number;

  constructor(private chatbotService: ChatbotService) { }

  ngOnInit() {

    this.latitude = 37.773972;
    this.longitude = -122.431297;
    this.zoom = 12;

    this.display_business_location();
  }

  display_business_location() {
    this.chatbotService.chatbotData$.subscribe(property => {
      this.propertyList = property.answer;
    })
  }

}
