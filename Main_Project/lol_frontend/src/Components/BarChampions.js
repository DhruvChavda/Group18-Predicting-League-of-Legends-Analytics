import React from "react";
import { Bar } from "react-chartjs-2";
import { ResponsiveContainer } from "recharts";

function BarChampions(props) {
    const dispVal = Object.values(props.data);
    const dispLab = Object.keys(props.data);

    return (
        <div style={{ width: "100%" }}>
            <ResponsiveContainer>
                <Bar
                    data={{
                        labels: dispLab,
                        datasets: [
                            {
                                label: "",
                                data: dispVal,
                                backgroundColor: [
                                    "rgba(255, 99, 132, 0.4)",
                                    "rgba(54, 162, 235, 0.4)",
                                    "rgba(255, 206, 86, 0.4)",
                                    "rgba(75, 192, 192, 0.4)",
                                    "rgba(153, 102, 255, 0.4)",
                                    "rgba(255, 159, 64, 0.4)",
                                ],
                                borderColor: [
                                    "rgba(255, 99, 132, 1)",
                                    "rgba(54, 162, 235, 1)",
                                    "rgba(255, 206, 86, 1)",
                                    "rgba(75, 192, 192, 1)",
                                    "rgba(153, 102, 255, 1)",
                                    "rgba(255, 159, 64, 1)",
                                ],
                                borderWidth: 1,
                            },
                        ],
                    }}
                    options={{
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true,
                            },
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: "Game Stats",
                            },
                        },
                    }}
                    // height={400}
                    // width={900}
                />
            </ResponsiveContainer>
        </div>
    );
}

export default BarChampions;
