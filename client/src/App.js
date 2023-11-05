import React, {useState, useEffect} from 'react'
// import dashboard from 'client/dashboard/dashboard.js'

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/member").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  
  return (
    <>

    {(typeof data.members === 'undefined') ? (
      <p>loading...</p>
    ): (
      data.members.map((member, i) => (
        <p key={i}>{member}</p>
      ))
    )}

     

    </>
  )
}

export default App
