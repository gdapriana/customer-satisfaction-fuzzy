import 'chart.js/auto';
import { Doughnut } from "react-chartjs-2";

export const Result = ({ result }: { result: any }) => {
    console.log(result)
    const data = {
        datasets: [
            {
                data: [result?.hasil || 4, 10 - result?.hasil || 4],
                backgroundColor: [
                    'rgba(67,67,67,0.2)',
                    'rgba(174,174,174,0.2)',
                ],
                borderColor: [
                    'rgba(174,174,174,0.2)',
                ],
                borderWidth: 1,
            },
        ],
    };
    return (
        <main className="flex w-1/3 gap-2 flex-col h-24 justify-center items-center">
            {result?.hasil && (
                <h1 className="font-bold">Result: {result?.hasil * 10}%</h1>
            )}
            <Doughnut data={data}/>
        </main>
    )
}