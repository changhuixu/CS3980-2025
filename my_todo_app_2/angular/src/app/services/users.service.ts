import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { map, Observable } from 'rxjs';
import { api } from './constants';

export interface LoginResult {
  username: string;
  role: string;
  access_token: string;
  token_type: string;
}

export interface UserDto {
  id: string;
  username: string;
  role: string;
  email: string;
}

@Injectable({
  providedIn: 'root',
})
export class UsersService {
  private readonly url = api + '/users';

  constructor(private http: HttpClient, private router: Router) {}

  signUp(username: string, password: string, email: string): Observable<any> {
    return this.http.post<any>(this.url + '/signup', {
      username,
      password,
      email,
    });
  }

  signIn(username: string, password: string): Observable<LoginResult> {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return this.http.post<LoginResult>(this.url + '/sign-in', formData).pipe(
      map((x) => {
        localStorage.setItem('user', JSON.stringify(x));
        return x;
      })
    );
  }
  logout() {
    localStorage.setItem('user', this._defaultUser);
    this.router.navigate(['login']);
  }

  get user(): LoginResult {
    const u = localStorage.getItem('user') || this._defaultUser;
    return JSON.parse(u);
  }

  private readonly _defaultUser: string =
    '{"username":"","role":"","access_token":"","token_type":""}';

  getAllUsers(): Observable<UserDto[]> {
    return this.http.get<UserDto[]>(this.url);
  }

  updateUserRole(id: string): Observable<any> {
    return this.http.post<any>(this.url + '/' + id, {});
  }
}
