import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AppConfig } from '../app-config';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatbotService {

  chatbotData$: Observable<any>;
  private chatbotDataSubject = new Subject<any>();

  constructor(private http: HttpClient, private appConfig: AppConfig) {
    this.chatbotData$ = this.chatbotDataSubject.asObservable();
  }

  send_message(message: string) {
    return this.http.get(this.appConfig.apiUrl + "/api/search/smart-agent/search/" + message)
  }

  send_data_to_map_component(data) {
    this.chatbotDataSubject.next(data);
  }
}


