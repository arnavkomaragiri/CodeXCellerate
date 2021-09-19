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
import './assets/css/Button.css';
import './assets/css/DropDown.css';


function App() {
  const [code, setCode] = useState("")
  const [selectedLang, setSelectedLang] = useState("Choose Language");
  const [selectedOperation, setSelectedOperation] = useState("Choose Service");
  const languages = ["C++", "Python", "JavaScript", "C"];
  const typeOfOperation = ["Time Complexity", "Explainability", "Plagiarism Detection"];

  // submit code to backend at port 8000
  const submitCode = (event) => { 
    async function fetchCopied(code) {
      const options = {
        method: 'POST',
        body: JSON.stringify({code}),
        headers: new Headers({ "Content-Type": "application/json"})
      }

      return await fetch(`http://localhost:8000/copied`, options)
      .then(response => response.json())
      // .then(({ value }) => {
      //   return value;
      // })
      .catch(err => {console.error(err)})
    }

    fetchCopied(code).then(function (data) {
      setCode(data);
      console.log(data);
      // document.getElementById('usercode').dangerouslySetInnerHTML = data;
      // console.log(data);
    })
  }

  return (
    <div>
      <div className="row1">
        <DropDown selected={selectedLang} setSelected={setSelectedLang} typeOfOptions={languages}/>
      </div>
      <div className="row2">
        <DropDown selected={selectedOperation} setSelected={setSelectedOperation} typeOfOptions={typeOfOperation}/>
      </div>
        
      <div className="rowBox">
      <button onClick={submitCode} className="button primary">Run Analysis</button>
        <form>
          <textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" id="usercode" className="design" rows="30" cols="50" required value={code} onChange={e => setCode(e.target.value)}></textarea>
        </form> 
        {/* <Button></Button> */}
      </div>
      
    </div>
  );
}

export default App;
