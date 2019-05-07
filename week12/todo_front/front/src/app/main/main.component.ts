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
  public loading = false;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
      setTimeout(()=>{
        this.loading = true;
      }, 2000);
    });
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

  
}