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

    const handleHiddenShow = (event) =>{
        let btns = document.querySelectorAll(`[id^='${event.target.id}']`)
        btns.forEach(btn =>{
            if(btn !== event.target){
                btn.classList.toggle('hidden')
            }
        })
    }
    const handleClickDeleteTask = (id : string) => {
        axios.delete(`http://localhost:8000/api/destroy/${id}/`)
        .then(
            respone =>{ console.log("DELETE SUCCESS: ", respone.status)
            fetchTask()
        }).catch(
            error => console.error("DELETE FAIL: ", error)
        );
    }
    const handleClickButtonDeleteTask = (e) =>{
        try{
            let id = e.target.id;
            if(id === 'undefined'){
                throw new Error("ID invalid");
            } 
            let clean_id = id.replace('delete_btn_',"");
            handleClickDeleteTask(clean_id)

        } catch (error) {
            console.error(error)
        }
    }
    const handleClickButtonEditTask = (e) =>{
        const paragraphs = document.querySelectorAll(`[id^='${e.target.id}']`);
        const textEdit = "Đang chỉnh sửa nhiệm vụ"
        const textView = "Không được chỉnh sửa nhiệm vụ"
        paragraphs.forEach(paragraph => {
            if(paragraph.getAttribute("contentEditable") ==="false"){
                paragraph.setAttribute("contentEditable", "true")
            }else{
                paragraph.setAttribute("contentEditable", "false")
            }
        })
        if(e.target.textContent === textEdit){
            e.target.textContent = textView
        }
        else{
            e.target.textContent = textEdit
        }
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
                <Button buttonOnClick={handleSubmit} buttonQuote="Thêm nhiệm vụ" className="ml-4"/>
            </Container>
            <Button id='view_btn_' buttonQuote="Xem nhiệm vụ" buttonOnClick={handleHiddenShow} className="mr-8"/>
            <Button id='delete_btn_' buttonQuote="Xóa nhiệm vụ" buttonOnClick={handleHiddenShow} className="mr-8"/>
            <Button id='edit_btn_' buttonQuote="Không được chỉnh sửa nhiệm vụ" buttonOnClick={handleClickButtonEditTask} />
            <br></br>
            <div id='view_btn_div' className='mt-6'>
                <ul className="text-green-600">
                    {tasks.map(task =>(
                        <li key={task.id}>
                            <Container className='justify-between'>
                                <strong>{task.time_start} </strong> <p id={`edit_btn_paragraph_${task.id}`} contentEditable={false}>{task.description_task}</p>
                                <Button id={`delete_btn_${task.id}`} buttonQuote="Delete" buttonOnClick={handleClickButtonDeleteTask}/>
                            </Container>
                        </li>
                    ))}
                </ul>
            </div>
        </>
    );
}