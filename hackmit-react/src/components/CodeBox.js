import '../assets/css/CodeBox.css'
import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';
// import react from 'react'
import { useState } from 'react';
// import { useEffect } from 'react';

function CodeBox(props){
    const [code, setCode] = useState("")
    // const [pretty, setPretty] = useState(code)

    // test code to check the input
    // useEffect(() => {
    //     console.log('render');
    // });


    return(
        <div className="container">
            <form>
                <textarea id="demo" className="design" rows="30" cols="50" required value={code} onChange={e => setCode(e.target.value)}></textarea>
            </form>
            <SyntaxHighlighter language="javascript" style={docco}>
                {code}
            </SyntaxHighlighter>
        </div>
        
    );
}

export default CodeBox;