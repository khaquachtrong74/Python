import { useEffect, useState } from "react";
import { Container, Header, Input, Button } from "./Components";
import axios from 'axios';

export function DashView(){
    const [tasks, setTasks] = useState([]);
    const [task, setTask] = useState('');
    const [inputTask, setInputTask] = useState('');
    const [isLoading, setIsLoading] = useState(true);
    const [isDeleting, setIsDeleting] = useState(false);
    const [isEditingTask, setIsEditingTask] = useState(false);
    const [error, setError] = useState(null);

    
    // GET METHOD
    const GETMethod = ()=>{
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
    // PUT METHOD
    const PUTMethod = (id : string) =>{
        axios.put(
        `http://localhost:8000/api/update/${id}/`,
        {
            description_task: task
        })
        .then(respone => {
            console.log("PUST SUCCESS: ",respone.data, respone.status);
            GETMethod();
        })
        .catch(error => console.error("PUT FAIL: ", error))
    };
    // POST METHOD
    const POSTMethod = ()=>{
        axios.post('http://localhost:8000/api/create/', {
            description_task: inputTask
        }).then(respone => {
            console.log("POST SUCCESS: ", respone.data)
            GETMethod()
            setInputTask('');
        }).catch(error =>
            console.error("POST FAIL: ", error)
        )
    }
    // DELETE METHOD
    const DELETEMethod = (id : string) => {
        axios.delete(`http://localhost:8000/api/destroy/${id}/`)
        .then(
            respone =>{ console.log("DELETE SUCCESS: ", respone.status)
            GETMethod()
        }).catch(
            error => console.error("DELETE FAIL: ", error)
        );
    }
    const handleChange = (event) =>{
        setInputTask(event.target.value);
    };
    const handleSubmit = (e)=>{
        if(e.target.textContent !== ''){
            POSTMethod()
        }
    }
    const handleClickButtonDeleteTask = (e) =>{
        let id = e.target.id;
        if(id === 'undefined'){
            throw new Error("ID invalid");
        } 
        let clean_id = id.replace('delete_btn_',"");
        DELETEMethod(clean_id)
    }
    
    useEffect(()=>{
        GETMethod()
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
            <Container className="justify-between">
                {/* <Label labelName="Task"/> *
                {/* Làm sao để nhận được dữ liệu từ thẻ Input đây */}
                <Input inputValue={inputTask} onChange={handleChange} placeHolder="Nhập task vào đây" type="text" className="w-2/3 p-2"/>
                    <Button 
                        buttonOnClick={handleSubmit} 
                        buttonQuote="Thêm nhiệm vụ" 
                        className="ml-4 border-1 transform transition-transform duration-200 hover:scale-110 min-w-24 whitespace-nowrap overflow-hidden text-ellipsis"/>
                    <div>
                        <Button 
                            buttonQuote={!isEditingTask ? "Tùy chỉnh" : "Chỉnh xong"} 
                            buttonOnClick={() => {
                                setIsDeleting(!isDeleting)
                                setIsEditingTask(!isEditingTask)
                            }} 
                            className="border-1 transform transition-transform duration-200 hover:scale-110 min-w-32 whitespace-nowrap overflow-hidden text-ellipsis"/>
                    </div>
            
            </Container>
            <br></br>
            <div id='view_btn_div' className='mt-12'>
                <ul className={!isEditingTask?"text-blue-100 duration-300 transition-all bg-gradient-to-l from-blue-600 to-purple-500 border-0 p-4 rounded-s-2xl rounded-e-2xl" : 
                    "bg-gradient-to-tl text-blue-100 from-blue-600 to-cyan-400 p-4 transition-all duration-300 rounded-2xl"}>
                    {tasks.map(task =>(
                        <li key={task.id}>
                            <Container className='justify-between grid grid-cols-3 text-center'>
                                <strong>{task.time_start} </strong> 
                                <p  
                                    contentEditable={isEditingTask}
                                    suppressContentEditableWarning={true}
                                    onInput={e => setTask(e.currentTarget.textContent)}
                                    className={isEditingTask ? "bg-gradient-to-b from-blue-500 to-sky-600 border-gray-200 transition-all rounded-md border-1 bg-teal-700 w-full text-white shadow-md p-3"
                                        : "p-3 border-1 rounded-md transition-all col-span-2 hover:bg-gradient-to-r hover:from-purple-500 hover:to-blue-500"
                                    }
                                >{task.description_task}</p>
                                <div className="">
                                    {isDeleting &&(
                                        <Button 
                                            id={`delete_btn_${task.id}`} 
                                            buttonQuote="Xóa" 
                                            buttonOnClick={handleClickButtonDeleteTask}
                                            className={isDeleting?"mr-8 p-4 bg-gradient-to-tl hover:scale-110 transition-all duration-300 text-pink-100 text-shadow-yellow-200 from-teal-400 to-blue-600":""}    
                                        />
                                    )}
                                    {isEditingTask && (
                                        <Button 
                                            buttonQuote="Lưu"
                                            buttonOnClick={() => {
                                                PUTMethod(task.id)
                                            }}
                                            className={isEditingTask?"p-4 bg-gradient-to-tl hover:scale-110 transition-all duration-300 text-pink-100 text-shadow-yellow-200 from-blue-400 to-purple-600":""}    
                                        />
                                    )}
                                </div>
                            </Container>
                        </li>
                    ))}
                </ul>
            </div>
        </>
    );
}