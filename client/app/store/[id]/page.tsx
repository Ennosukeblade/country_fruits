import React from 'react'
interface IProduct {
    id: number
    name: string
    price: number
    description: string
    image: string
}
const page = async ({ params }: { params: { id: number } }) => {
    const getProduct = async () => {
        const res = await fetch(`http://127.0.0.1:8000/store/${params.id}`)
        //const parsedData = JSON.parse(products.data);
        console.log(res);
        const result = await res.json()
        console.log("THIS IS MY PRODUCT***********hhhh", result);
        return result
    }
    const product: IProduct = await getProduct()
    console.log(product);
    return (
        <div>Product ID: {params.id}
            <h1>{product.name}</h1>
        </div>
    )
}

export default page