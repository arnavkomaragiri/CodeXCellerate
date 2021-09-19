import { useState } from 'react';
import './App.css';
import DropDown from './components/DropDown.js';
// import Prettify from './components/Prettify.js';
import CodeBox from './components/CodeBox.js';
import './assets/css/CodeBox.css'
import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';
// import react from 'react'
// import { useEffect } from 'react';


function App() {
  const [code, setCode] = useState("")
  const [machineCode, setMachineCode] = useState("")
  const [selectedLang, setSelectedLang] = useState("Choose");
  const [selectedOperation, setSelectedOperation] = useState("Choose");
  const languages = ["C++", "Python", "JavaScript", "C"];
  const typeOfOperation = ["Time Complexity", "Explainability", "Plagiarism Detection"];

  // submit code to backend at port 8000
  const submitCode = (event) => {
    if (typeOfOperation === "Time Complexity") {
      var response = fetch('http://localhost:8000/runtime', 
                      {
                        method: 'POST',
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({"code": code})
                      })
    }
  }

  return (
       <div>
          <div className="rowDropDown">
            <DropDown selected={selectedLang} setSelected={setSelectedLang} typeOfOptions={languages}/>
            <DropDown selected={selectedOperation} setSelected={setSelectedOperation} typeOfOptions={typeOfOperation}/>
          </div>
          {/* <Prettify></Prettify> */}
          <div className="row">
            <div className="container">
              <form>
                  <textarea id="usercode" className="design" rows="30" cols="50" required value={code} onChange={e => setCode(e.target.value)}></textarea>
              </form>
              <SyntaxHighlighter language="javascript" style={docco}>
                  {code}
              </SyntaxHighlighter>
            </div>
            <button onClick={submitCode}>
              Run Analysis
            </button>
            <div className="container">
              <SyntaxHighlighter language="javascript" style={docco}>
                  {machineCode}
              </SyntaxHighlighter>
            </div>
            
          </div>
      </div>
  );
}

export default App;
