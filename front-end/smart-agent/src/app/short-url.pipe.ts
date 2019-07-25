import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'shortUrl'
})
export class ShortUrlPipe implements PipeTransform {

  transform(url: string, args?: any): any {
    if (url) {
      const len = url.length;
      if (len > 30) // only shorten if greater than 30
        // change value 21 and 9 as per requirement
        return url.substr(0, 5) + '...' + url.substring(len - 50, len);
      return url;
    }
    return url;
  }
}