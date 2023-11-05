import * as React from 'react';
import { useTheme } from '@mui/material/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';
import Title from './title';
// fetch("data.json")
//   .then((response) => response.json())
//   .then((json) => console.log);

import jsonData from "./data.json";
console.log(jsonData.hourly.time);


// Generate Sales Data
function createData(time, amount) {
  return { time, amount };
}

const data = [
  createData(12, jsonData.hourly.temperature_2m[12]),
  createData('03:00', jsonData.hourly.temperature_2m[12 + 24]),
  createData('06:00', jsonData.hourly.temperature_2m[12 + 48]),
  createData('09:00', jsonData.hourly.temperature_2m[12 + 72]),
  createData('12:00', jsonData.hourly.temperature_2m[12 + 96]),
  createData('15:00', jsonData.hourly.temperature_2m[12 + 120]),
  createData('18:00', jsonData.hourly.temperature_2m[12 + 144]),
  createData('21:00', jsonData.hourly.temperature_2m[12 + 168]),
  createData('24:00', undefined),
];

export default function Chart() {
  const theme = useTheme();

  return (
    <React.Fragment>
      <Title>Two Week Forecast</Title>
      <ResponsiveContainer>
        <LineChart
          data={data}
          margin={{
            top: 13,
            right: 10,
            bottom: 0,
            left: 15,
          }}
        >
          <XAxis
            dataKey="time"
            stroke={theme.palette.text.secondary}
            style={theme.typography.body2}
          />
          <YAxis
            stroke={theme.palette.text.secondary}
            style={theme.typography.body2}
          >
            <Label
              angle={270}
              position="left"
              style={{
                textAnchor: 'middle',
                fill: theme.palette.text.primary,
                ...theme.typography.body1,
              }}
            >
              Temp, Soil Temp (C)
            </Label>
          </YAxis>
          <Line
            isAnimationActive={true}
            type="monotone"
            dataKey="amount"
            stroke={theme.palette.primary.main}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </React.Fragment>
  );
}
