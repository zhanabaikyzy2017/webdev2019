import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service'
import {TaskList, Task,IAuthResponse} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http:HttpClient) {
    super(http);
  }
  

  getTaskLists() : Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/task_lists/',{});
  }

  getTasks(id:number):Promise<Task[]>{
    console.log("asdasd");
    return this.get(`http://localhost:8000/api/task_lists/${id}/tasks/`,{})
   // console.log("asdasd");
  }

  createTaskList(name:any): Promise<TaskList>{
    return this.post('http://localhost:8000/api/task_lists/',{
      name:name
    });
  } 

  updateTaskList(taskList:TaskList):Promise<TaskList>{
    return this.put(`http://localhost:8000/api/task_lists/${taskList.id}`,{
      name: taskList.name
    });
  }


  deleteTaskList(id:number):Promise<any>{
    return this.delet(`http://localhost:8000/api/task_lists/${id}`,{});
  }

  auth(login:string,password:string):Promise<IAuthResponse>{
    return this.post('http://localhost:8000/api/login/',{
      username:login,
      password:password
    });
  }

  
  logout():Promise<any>{
    return this.post('http://localhost:8000/api/logout/',{})
  }

} 