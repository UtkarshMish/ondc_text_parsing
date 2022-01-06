import axios from "axios";
export async function getProducts(pageNo = 1) {
	try {
		const response = await axios.get("/api/products?page=" + pageNo);
		if (response.data) {
			return [response.data.products, response.data.total];
		}
	} catch (err) {
		console.log("error: ", err);
	}
	return [null, null];
}
