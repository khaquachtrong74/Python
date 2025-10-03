import { Container, Input, Label } from './Components';
export function ViewLoginPage(){
    const LoginContainer = () => (
        <div className='w-full h-screen flex items-center  justify-center bg-gray-100'>
            <form className='w-fit h-1/3 bg-white p-8 rounded-lg shadow-md'>
                <Container> 
                    <Label labelName='Tài khoản' isRequired={true}></Label>
                    <Input placeHolder='Điền tài khoản vào đây' isRequired={true}></Input>
                </Container>
                <Container> 
                    <Label labelName='Mật khẩu' isRequired={true}></Label>
                    <Input placeHolder='Điền mật khẩu vào đây' type='password' isRequired={true}></Input>
                </Container>
            <button>Click Me!</button>
            </form>
        </div>
    )
    return (
        <>
            <LoginContainer />
        </>
    )
}