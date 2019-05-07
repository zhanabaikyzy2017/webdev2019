import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service'
import {TaskList, Task} from '../models/models';

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
    return this.get(`http://localhost:8000/api/task_lists/${id}/tasks/`,{})
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


} 