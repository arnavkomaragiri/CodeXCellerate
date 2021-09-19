import { useState } from 'react';
import '../assets/css/DropDown.css'

function DropDown({ selected, setSelected, typeOfOptions}){
  const [isActive, setActive] = useState(false);
  // const options = ["C++", "Python", "JavaScript", "C"];
  const options = typeOfOptions;

  return(
    <div className="dropDown">
      <div className="dropDown-button" onClick={(e)=>setActive(!isActive)}>
        {selected}
        <span className="fa"></span>
      </div>
      {isActive && (
        <div className="dropDown-content">
          {options.map((option) => (
            <div onClick={(e)=>{
              setSelected(option);
              setActive(false);
            }} className="dropDown-item">
              {option}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default DropDown;