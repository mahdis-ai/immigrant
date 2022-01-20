import React, { useState } from 'react';
import TextField from "@material-ui/core/TextField";

const SignUp = () => {
  const [name, setName] = useState("");
  const [pass, setPass] = useState("");
  const [mobile, setMobile] = useState("");
  return (
    <div
    style={{
     
      display: 'flex',
      justifyContent: 'Center',
      alignItems: 'Center',
      height: '100vh',
   
    }}
  >
    
   <div 
   style={{
    
        
textAlign: 'center',    
  
    
  }}
>


      <h2>ثبت نام</h2>
      <TextField
        value={name}
        label="نام کاربری"
        onChange={(e) => {
          setName(e.target.value);
        }}
      />
      <h3>نام کاربری: {name} </h3>


      
      <TextField
        value={pass}
        label="رمز"
        onChange={(e) => {
          setPass(e.target.value);
        }}
      />
      <h3>رمز: {pass} </h3>


      <TextField
        value={mobile}
        label="موبایل"
        onChange={(e) => {
          setMobile(e.target.value);
        }}
      />
      <h3>موبایل: {mobile} </h3>




    </div>
    </div>
  );
};
  
export default SignUp;