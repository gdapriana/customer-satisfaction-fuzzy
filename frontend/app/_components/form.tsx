import {Label} from "@/components/ui/label";
import {Input} from "@/components/ui/input";
import {Dispatch, FormEvent, SetStateAction} from "react";
import {Button} from "@/components/ui/button";

export const Form = ({ setResult }: { setResult: Dispatch<SetStateAction<any>> }) => {
    const onSubmit = async (e: any) => {
        e.preventDefault();
        const kualitas_makanan = e.target.k_m.value
        const kecepatan_layanan = e.target.k_p.value
        const response = await fetch(`http://127.0.0.1:5000/predict`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "POST", body: JSON.stringify({kualitas_makanan: parseFloat(String(kualitas_makanan)), kecepatan_layanan: parseFloat(kecepatan_layanan)}) })
            .then((res) => res.json())

        setResult(response);
    }

    return (
        <form onSubmit={onSubmit} method="POST" className="flex w-2/3 gap-4 flex-col justify-start items-stretch">
            <div className="flex gap-2 flex-col justify-center items-start">
                <Label className="font-bold">Kualitas Makanan</Label>
                <Input required step="0.01" type="number" name="k_m"/>
            </div>
            <div className="flex gap-2 flex-col justify-center items-start">
                <Label className="font-bold">Kecepatan Pelayanan (menit)</Label>
                <Input required step="0.01" type="number" name="k_p"/>
            </div>
            <Button type="submit" size="sm" variant="secondary">Check</Button>
        </form>
)
}