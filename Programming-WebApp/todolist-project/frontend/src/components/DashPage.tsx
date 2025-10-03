import { useEffect, useState } from "react";
import { Container, Header, Input, Button } from "./Components";
import axios from 'axios';

export function DashView(){
    const [tasks, setTasks] = useState([]);
    const [inputTask, setInputTask] = useState('');
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    const handleChange = (event) =>{
        setInputTask(event.target.value);
    };
 
    const handleSubmit = ()=>{
        axios.post('http://localhost:8000/api/create/', {
            description_task: inputTask
        }).then(respone => {
            console.log("POST SUCCESS: ", respone.data)
            fetchTask()
            setInputTask('');
        }).catch(error =>
            console.error("POST FAIL: ", error)
        )
    }
    const fetchTask = ()=>{
        fetch(
            'http://localhost:8000/api/todo-list'
        ).then(respone =>{
            if(!respone.ok){
                throw new Error('Không thể tải dữ liệu');
            }
            return respone.json();
        }).then(data => {
            setTasks(data);
            setIsLoading(false);
        }).catch(error =>{
            console.error("Lỗi lạ: ", error);
            setError(error.message);
            setIsLoading(false);
        });
    }
    useEffect(()=>{
        fetchTask()
    },[]) //  [] để đảm bảo chỉ chạy 1 lần duy nhất khi component mount
    if(isLoading){
        return <div>Đang tải dữ liệu...</div>
    }
    if(error){
        return <div>Lỗi: {error}</div>
    }
    return(
        <>
            <Header
                title="Chào mừng bạn tới với trang tổng quan"
            ></Header>
            {/* Cần Input ở đây */}
            <Container>
                {/* <Label labelName="Task"/> */}
                {/* Làm sao để nhận được dữ liệu từ thẻ Input đây */}
                <Input inputValue={inputTask} onChange={handleChange} placeHolder="Nhập task vào đây" type="text"/>
                <Button buttonOnClick={handleSubmit} buttonQuote="Click me!"/>
            </Container>

            <div>
                <ul className="text-green-600">
                    {tasks.map(task =>(
                        <li key={task.id}>
                            <strong>{task.time_start} : {task.description_task}</strong>
                        </li>
                    ))}
                </ul>
            </div>
        </>
    );
}