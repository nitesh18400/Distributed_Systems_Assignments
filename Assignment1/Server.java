import java.io.*;
import java.net.*;
import java.util.Scanner;

class ClientHandle extends Thread
{
    final DataInputStream inpt;  // Messages from client Data Stream
    final Socket s;  // Socket Object
    final String name;  // Client Name
    ClientHandle(Socket s,DataInputStream inpt,String name)  // Constructor
    {
        this.inpt=inpt;
        this.s=s;
        this.name=name;
    }
    @Override
    public void run()
    {
        while(true)
        {
            String messege_from_client="";   
            try 
            {
                messege_from_client = inpt.readUTF();  // reading message from client
            } catch (IOException e1) 
            {
                e1.printStackTrace();
            }
            if(messege_from_client.equals("quit"))  // Close connection request from a client
            {
                System.out.println("Received a close connection request from Client "+ this.name);
                System.out.println("Closing the connections");
                try 
                {
                    this.s.close();
                } catch (IOException e) 
                {
                    e.printStackTrace();
                }
                System.out.println("Closed");
                break;
                
            }
            else
            {
                System.out.println(this.name+":"+messege_from_client);  // print message from client
            }

        }
        try 
        {
            inpt.close();   //closing datastream
        } catch (IOException e) 
        {
            e.printStackTrace();
        }
        

    }


}
public class Server
{
    static int cnt=0;  // Count of Connected Client
    public static void main(String[] args)  throws IOException
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Port No:");
        int port=sc.nextInt();
        ServerSocket server_sokt=new ServerSocket(port); //Server Created 
        System.out.println("Server Hosted at Port "+port);

        while(true)
        {
            Socket socket_object=null; // Initialize Listening Socket
            try 
            {
                socket_object=server_sokt.accept();  //Accept Connection Request from Client
                cnt+=1;  
                DataInputStream inpt=new DataInputStream(socket_object.getInputStream());
                // String name="Client"+cnt;  // I can also put names like client1,client2 ......
                String name=inpt.readUTF();   // Read Name of Client 
                System.out.println("Client "+name+" Connected"); 
                Thread new_client_thread=new ClientHandle(socket_object,inpt,name); // Creating a thread for a client
                new_client_thread.start(); //starting thread
            } 
            catch (Exception e)
            {
                socket_object.close();
                e.printStackTrace();
                break;
            }
        }
        server_sokt.close();
        sc.close();
    }
}