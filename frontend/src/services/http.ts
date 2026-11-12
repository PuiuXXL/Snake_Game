import { API_URL } from '../config/api'

export class ApiError extends Error {
  status?: number

  constructor(message: string, status?: number) {
    super(message)
    this.status = status
  }
}

export async function postJson<T>(path: string, body?: unknown): Promise<T> {
  let response: Response
  try {
    response = await fetch(`${API_URL}${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: body === undefined ? undefined : JSON.stringify(body),
    })
  } catch {
    throw new ApiError(
      `Nu mă pot conecta la backend (${API_URL}). Rulează uvicorn?`,
    )
  }

  if (!response.ok) {
    let detail = `Eroare ${response.status}`
    try {
      const data = await response.json()
      if (typeof data.detail === 'string') detail = data.detail
    } catch {
      // răspunsul nu e JSON; păstrăm mesajul implicit
    }
    if (response.status === 501) {
      // Detaliul (ce funcție lipsește) rămâne în consola browserului,
      // nu în interfață.
      console.warn(detail)
    }
    throw new ApiError(detail, response.status)
  }

  return response.json() as Promise<T>
}
