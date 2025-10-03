import type React from "react";

type LabelProps ={
    labelName : string,
    isRequired?: boolean;
}
type InputProps = {
        placeHolder :  string,
        type?: 'text' | 'password' | 'email',
        isRequired?: boolean,
        inputValue?: string,
        onChange?: (event : React.ChangeEvent<HTMLInputElement>) => void,
    } ;
type ButtonProps = {
    buttonQuote : string,
    buttonOnClick?:(event: React.MouseEvent<HTMLButtonElement, MouseEvent>) =>void,
}
type Title = {
    title : string
};
export const Label = ({labelName, isRequired}:LabelProps) =>(
    <label htmlFor={labelName} className='mb-1 text-sm font-medium'>
        {labelName}{isRequired && <span className='text-red-500'> * </span>} 
    </label>
)
export const Input = ({placeHolder,  type='text', isRequired=false, inputValue="", onChange = () =>{}} : InputProps) =>(
    <input 
        type={type} 
        placeholder={placeHolder} 
        required={isRequired}
        value={inputValue}
        onChange={onChange}
        className='px-3 py-2 border border-gray-300 rounded-md'
    />
);
export const Button = ({buttonQuote, buttonOnClick}:ButtonProps) =>(
    <button onClick={buttonOnClick} className="text-white p-3 rounded-md ml-4 bg-gray-600 button-hover">
        {buttonQuote}
    </button>
)

export function Container({children}){ 
    return(
        <div className="flex flex-row  items-center mt-6 mb-8  w-full">
            {/* Đặt các componnet vào đây */}
            {children}
        </div>
    )
}

export const Header = ({title}:Title)=>(
    <h1
        className="text-2xl text-shadow-black p-4"
    >
        {title}
    </h1>
);