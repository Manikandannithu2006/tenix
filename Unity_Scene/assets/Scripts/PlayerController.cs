using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float lookSpeed = 2f;
    public float moveSpeed = 3f;

    float rotX = 0f, rotY = 0f;

    void Start() { Cursor.lockState = CursorLockMode.Locked; }

    void Update()
    {
        rotX += Input.GetAxis("Mouse X") * lookSpeed;
        rotY -= Input.GetAxis("Mouse Y") * lookSpeed;
        rotY = Mathf.Clamp(rotY, -80, 80);
        transform.localRotation = Quaternion.Euler(rotY, rotX, 0);

        Vector3 forward = transform.forward * Input.GetAxis("Vertical");
        Vector3 right = transform.right * Input.GetAxis("Horizontal");
        transform.position += (forward + right) * moveSpeed * Time.deltaTime;
    }
}
