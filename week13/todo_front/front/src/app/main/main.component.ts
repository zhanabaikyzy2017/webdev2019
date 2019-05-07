import { Component, OnInit } from '@angular/core';
import {TaskList, Task} from '../models/models';
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public taskLists: TaskList[] = [];
  public tasks: Task[] = [];
  public name: any = '';
  //public loading = false;
  public logged = false;

  public login: any = '';
  public password: any = '';
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if(token){
      this.logged = true;
    }  
    if(this.logged){
      this.getTaskLists();
    }
     
  }
  getTaskLists(){
    this.provider.getTaskLists().then(res=>{
      this.taskLists = res;
      //this.loading = true;
    })
  }
  
  getTaskOfTaskList(taskList: TaskList) {
    this.provider.getTasks(taskList.id).then(res => {this.tasks = res; });
  }

  updateTaskList(c:TaskList){
    this.provider.updateTaskList(c).then(res=>{
      console.log(c.name + 'updated');
    });
  }
  deleteTaskList(c:TaskList){
    this.provider.deleteTaskList(c.id).then(res=>{
      console.log(c.name + ' deleted');
      this.provider.getTaskLists().then(r=>{
        this.taskLists = r;
      });
    });
  }
  createTaskList(){
    if(this.name!==''){
      this.provider.createTaskList(this.name).then(res=>{
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }

  auth(){
    if(this.login !== '' && this.password !== '' ){
      console.log("asd");
      this.provider.auth(this.login,this.password).then(res=>{
        localStorage.setItem('token',res.token);
        this.logged = true;
        this.getTaskLists();
      });  
    }
  }
  logout(){
    this.provider.logout().then(res=>{
      localStorage.clear();
      this.logged = false;
    })
  }

  
}