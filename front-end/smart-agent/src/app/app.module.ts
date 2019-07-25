import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ChatbotComponent } from './components/chatbot/chatbot.component';
import { HeaderComponent } from './components/header/header.component';
import { AppConfig } from './app-config';
import { ShortUrlPipe } from './short-url.pipe';
import { MapComponent } from './components/map/map.component';
import { AgmCoreModule } from '@agm/core';
import { AgmSnazzyInfoWindowModule } from '@agm/snazzy-info-window';


@NgModule({
  declarations: [
    AppComponent,
    ChatbotComponent,
    HeaderComponent,
    ShortUrlPipe,
    MapComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    AgmCoreModule.forRoot({
      apiKey: 'REPLACE_WITH_YOUR_GOOGLE_MAP_API_KEY'
    }),
    AgmSnazzyInfoWindowModule,
    
  ],
  providers: [AppConfig],
  bootstrap: [AppComponent]
})
export class AppModule { }
