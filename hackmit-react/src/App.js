import { useState } from 'react';
import './App.css';
import DropDown from './components/DropDown.js';
// import Prettify from './components/Prettify.js';
import CodeBox from './components/CodeBox.js';

function App() {
  const [selectedLang, setSelectedLang] = useState("Choose");
  const [selectedOperation, setSelectedOperation] = useState("Choose");
  const languages = ["C++", "Python", "JavaScript", "C"];
  const typeOfOperation = ["Multiprocessing", "Time Complexity", "Explainability"];

  return (
       <div>
          <div className="rowDropDown">
            <DropDown selected={selectedLang} setSelected={setSelectedLang} typeOfOptions={languages}/>
            <DropDown selected={selectedOperation} setSelected={setSelectedOperation} typeOfOptions={typeOfOperation}/>
          </div>
          {/* <Prettify></Prettify> */}
          <div className="row">
            <CodeBox></CodeBox>
            <CodeBox></CodeBox>
          </div>
      </div>
  );
}

export default App;
