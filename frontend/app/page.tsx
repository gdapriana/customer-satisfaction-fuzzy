'use client'
import { Form } from "@/app/_components/form"
import { Result } from "@/app/_components/result"
import {useState} from "react";
import Image from "next/image";

export default function Home() {

    const [result, setResult] = useState<any>()

  return (
      <main className="h-screen pt-12 w-full flex justify-start flex-col overflow-auto p-4 items-center">
          <div className="w-full gap-8 flex-col max-w-xl flex justify-start items-center">
              <h1 className="font-bold text-lg">Menilai Tingkat Kepuasan Pelanggan di Restoran</h1>
              <div className="flex w-full gap-8 justify-center items-center">
                  <Form setResult={setResult} />
                  <Result result={result} />
              </div>
              {result && (
                  <div className="flex justify-start flex-col gap-2">
                      <div className="flex flex-col justify-start items-center">
                          <h1 className="font-bold">Derajat Keanggotaan Kualitas Makanan</h1>
                          <p>Buruk: {result.derajat_kualitas.buruk.toFixed(2)}</p>
                          <p>Sedang: {result.derajat_kualitas.sedang.toFixed(2)}</p>
                          <p>Baik: {result.derajat_kualitas.baik.toFixed(2)}</p>
                      </div>
                      <div className="flex flex-col justify-start items-center">
                          <h1 className="font-bold">Derajat Keanggotaan Kecepatan Pelayan</h1>
                          <p>Cepat: {result.derajat_kecepatan.cepat.toFixed(2)}</p>
                          <p>Lambat: {result.derajat_kecepatan.lambat.toFixed(2)}</p>
                      </div>
                  </div>
              )}
              <Image src="/output.png" alt="gambar" width={1000} height={1000} />
          </div>
      </main>
  );
}
