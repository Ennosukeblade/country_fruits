'use client'
import { useEffect, useState } from "react";
import Link from "next/link";

const getProducts = async () => {
    const res = await fetch('http://127.0.0.1:8000/store')
    const products = await res.json()
    //const parsedData = JSON.parse(products.data);
    console.log("THIS IS MY DATA", products);

    return products
}
interface IProduct {
    id: number
    name: string
    price: number
    description: string
    image: string

}
export default function StorePage() {
    const [products, setProducts] = useState<Array<IProduct>>([])
    useEffect(() => {
        getProducts().then((res: Array<IProduct>) => {
            console.log(res)
            setProducts(res)
        }).catch(err => console.log(err))
    }, [])
    console.log(products);

    //const products: Array<IProduct> = await getProducts()
    return (
        <div className="container">
            <div className="flex flex-wrap">
                {products.map((p, i) => (
                    <div key={i} className="w-full md:w-1/2 lg:w-1/4 rounded-md shadow-md dark:dark:bg-gray-900 dark:dark:text-gray-100">
                        <Link href={`/store/${p.id}`}>
                            <img src={`http://127.0.0.1:8000/static/img/${p.image}`} alt="" className="object-cover object-center w-full rounded-t-md h-72 dark:dark:bg-gray-500" />
                        </Link>
                        <div className="flex flex-col justify-between p-6 space-y-8">
                            <div className="space-y-2">
                                <h2 className="text-3xl font-semibold tracki">{p.name}</h2>
                                <h3 className="text-xl font-semibold color">{p.price}</h3>
                                <p className="dark:dark:text-gray-100">{p.description}</p>
                            </div>
                            <button type="button" className="flex items-center justify-center w-full p-3 font-semibold tracki rounded-md dark:dark:bg-violet-400 dark:dark:text-gray-900">Read more</button>
                        </div>
                    </div>
                ))}
            </div>
        </div>

    )
}
