import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';
// import { useState } from 'react';

function Prettify(){
    const codeString = `function createStyleObject(classNames, style) {
        return classNames.reduce((styleObject, className) => {
          return {...styleObject, ...style[className]};
        }, {});
      }`;

    // const [code, setCode] = useState("")

    return(
        <SyntaxHighlighter language="javascript" style={docco}>
            {codeString}
        </SyntaxHighlighter>
    );
};

export default Prettify;