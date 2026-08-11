import { useState } from "react";
import Plot from "react-plotly.js";
import "./App.css";


function App() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);



  const uploadFile = async () => {

    if (!file) {
      alert("Please select CSV file");
      return;
    }


    const formData = new FormData();

    formData.append(
      "file",
      file
    );


    const response = await fetch(
      "http://127.0.0.1:8000/analyze",
      {
        method: "POST",
        body: formData
      }
    );


    const data = await response.json();

    setResult(data);

  };



  return (

    <div className="dashboard">


      <h1>
        ☁️ Cloud Data Analytics Dashboard
      </h1>



      <div className="upload-card">

        <input
          type="file"
          accept=".csv"
          onChange={
            (e)=>setFile(e.target.files[0])
          }
        />


        <button onClick={uploadFile}>
          Upload & Analyze
        </button>

      </div>



      {
        result &&

        <>


        <div className="cards">


          <div className="card">
            <h3>Rows</h3>
            <p>{result.rows}</p>
          </div>


          <div className="card">
            <h3>Columns</h3>
            <p>{result.columns}</p>
          </div>


          <div className="card">
            <h3>File</h3>
            <p>{result.filename}</p>
          </div>


        </div>



        <div className="info">


          <h2>
            Column Names
          </h2>


          <p>
            {
              result.column_names.join(", ")
            }
          </p>



          <h2>
            Missing Values
          </h2>


          <pre>
          {
            JSON.stringify(
              result.missing_values,
              null,
              2
            )
          }
          </pre>


        </div>



        <div className="charts">


          {
            result.charts.scatter &&

            <Plot
              data={
                result.charts.scatter.data
              }

              layout={{
                ...result.charts.scatter.layout,
                width:500,
                height:400
              }}

            />

          }



          {
            result.charts.histogram &&

            <Plot
              data={
                result.charts.histogram.data
              }

              layout={{
                ...result.charts.histogram.layout,
                width:500,
                height:400
              }}

            />

          }



          {
            result.charts.bar &&

            <Plot
              data={
                result.charts.bar.data
              }

              layout={{
                ...result.charts.bar.layout,
                width:500,
                height:400
              }}

            />

          }


        </div>


        </>

      }


    </div>

  );

}


export default App;