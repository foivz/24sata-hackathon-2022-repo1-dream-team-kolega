package com.example.financije;

import static com.example.financije.ProduktActivity.PRODUKT_ID_KEY;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.util.ArrayList;

public class ShoppingViewAdapter extends RecyclerView.Adapter<ShoppingViewAdapter.ViewHolder>{

    private ArrayList<Baza> produkt = new ArrayList<>();
    private ArrayList<Baza> favorit = new ArrayList<>();
    private Context nContext;

    public ShoppingViewAdapter(Context nContext) {
        this.nContext = nContext;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.list_shop, parent,false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, final int position) {
        holder.txtIme.setText(produkt.get(position).getName());
        holder.txtCijena.setText(produkt.get(position).getPrice());
        Glide.with(nContext)
                .asBitmap()
                .load(produkt.get(position).getLink())
                .into(holder.imgShop);
        holder.parent.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(nContext, ProduktActivity.class);
                intent.putExtra(PRODUKT_ID_KEY,produkt.get(position).getId());
                nContext.startActivity(intent);
            }
        });
        holder.add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(nContext, "dodano", Toast.LENGTH_SHORT).show();
            }
        });

    }

    @Override
    public int getItemCount() {
        return produkt.size();
    }

    public ShoppingViewAdapter(ArrayList<Baza> favorit) {
        this.favorit = favorit;
    }

    public void setProdukt(ArrayList<Baza> produkt) {
        this.produkt = produkt;
        notifyDataSetChanged();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{
        private CardView parent;
        private ImageView imgShop;
        private TextView txtIme;
        private TextView txtCijena;
        private ImageView add;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            parent = itemView.findViewById(R.id.parent);
            imgShop = itemView.findViewById(R.id.imgShop);
            txtIme = itemView.findViewById(R.id.textProdukt);
            txtCijena = itemView.findViewById(R.id.textcijena);
            add = itemView.findViewById(R.id.add1);

        }
    }
}
