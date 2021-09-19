import { useState } from 'react';
import './App.css';
import DropDown from './components/DropDown.js';
import CodeBox from './components/CodeBox.js';
import './assets/css/CodeBox.css'
import './assets/css/Button.css';
import './assets/css/DropDown.css';


function App() {
  const [code, setCode] = useState("")
  const [selectedLang, setSelectedLang] = useState("Choose Language");
  const [selectedOperation, setSelectedOperation] = useState("Choose Service");
  const languages = ["C++", "C", "Python", "JavaScript"];
  const typeOfOperation = ["Time Complexity", "Explainability", "Plagiarism Detection"];

  async function fetchCopied(code) {
    const options = {
      method: 'POST',
      body: JSON.stringify({"code": code}),
      headers: new Headers({ "Content-Type": "application/json"})
    }

    return await fetch(`http://localhost:8000/copied`, options)
    .then(response => response.json())
    .catch(err => {
      console.error(err);
    });
  }

  fetchCopied(code).then(function (data) {
    setCode(data);
    console.log(data);
    // document.getElementById('usercode').dangerouslySetInnerHTML = data;
    // console.log(data);
  })

  return (
    <div className="float-container">
      <div className="float-child">
        <DropDown selected={selectedLang} setSelected={setSelectedLang} typeOfOptions={languages}/>
        <DropDown selected={selectedOperation} setSelected={setSelectedOperation} typeOfOptions={typeOfOperation}/>
        <button onClick={fetchCopied()} className="button primary">Run Analysis</button>
      </div>
      <div className="float-child">
          <textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" id="usercode" className="design" rows="30" cols="50" required value={code} onChange={e => setCode(e.target.value)}></textarea>
      </div>
      </div>
  );
}

export default App;
