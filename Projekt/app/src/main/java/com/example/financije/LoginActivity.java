package com.example.financije;

import androidx.appcompat.app.AppCompatActivity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.util.LinkedList;
import java.util.List;

class User{
    String name,password;

    public void setName(String name) {
        this.name = name;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getName() {
        return name;
    }

    public String getPassword() {
        return password;
    }

    public User(String name, String password) {

        this.name = name;
        this.password = password;
    }
}
public class LoginActivity extends AppCompatActivity {


    private TextView loginText,family,password;
    private Button login,register,confirm;
    private int havzAccount=0;
    //TODO:Spoji s bazom;
    List<User> users = new LinkedList<User>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        Button next = (Button) findViewById(R.id.Register);
        users.add(new User("Savoric","123"));
        users.add(new User("Belina","123"));
    }
    public void Login(View view){
        loginText= findViewById(R.id.textAuta);
        login= findViewById(R.id.Login);
        register= findViewById(R.id.Register);
        confirm= findViewById(R.id.Confirm);
        family= findViewById(R.id.ImeAuta);
        password= findViewById(R.id.Password);
        loginText.setTextScaleX(0);
        login.setScaleX(0);
        register.setScaleX(0);
        confirm.setScaleX(1);
        family.setScaleX(1);
        password.setScaleX(1);
        havzAccount=1;

    }
    public void Register(View view){
        loginText= findViewById(R.id.textAuta);
        login= findViewById(R.id.Login);
        register= findViewById(R.id.Register);
        confirm= findViewById(R.id.Confirm);
        family= findViewById(R.id.ImeAuta);
        password= findViewById(R.id.Password);
        loginText.setTextScaleX(0);
        login.setScaleX(0);
        register.setScaleX(0);
        confirm.setScaleX(1);
        family.setScaleX(1);
        password.setScaleX(1);

    }
    public void Continue(View view){
        int succes=0;
        family= findViewById(R.id.ImeAuta);
        password= findViewById(R.id.Password);

        if(havzAccount==1) {
            for (int i = 0; i < users.size(); i++) {
                if (users.get(i).getName().toString().equals(family.getText().toString())) {
                    //TODO:Secure password
                    if (users.get(i).getPassword().toString().equals(password.getText().toString())) {
                        succes = 2;
                    } else {
                        succes = 1;
                    }
                }
            }
            if (succes == 0) {
                Toast.makeText(this, family.getText().toString() + " ne postoji", Toast.LENGTH_SHORT).show();
            } else if (succes == 1) {
                Toast.makeText(this, family.getText().toString() + " posoji ali je sifra kriva", Toast.LENGTH_SHORT).show();
            } else {

                Toast.makeText(this, family.getText().toString() + " posoji i sifra je dobra", Toast.LENGTH_SHORT).show();
                Intent intent=new Intent(LoginActivity.this,MainActivity.class);
                startActivity(intent);
            }
        }
        else {
            for(int i=0;i<users.size();i++){
                if(users.get(i).getName().toString().equals(family.getText().toString())){
                    succes=1;
                }
            }
            if(succes==1) Toast.makeText(this, "Taj korisnik vec postoji", Toast.LENGTH_SHORT).show();
            else {
                Toast.makeText(this, "Registrirani ste. Nastavljamo na postavke obitelji i prijevoza", Toast.LENGTH_SHORT).show();
                users.add(new User(family.getText().toString(),password.getText().toString()));
                Intent intent=new Intent(LoginActivity.this,AutoActivity.class);
                startActivity(intent);

            }
        }
    }
}