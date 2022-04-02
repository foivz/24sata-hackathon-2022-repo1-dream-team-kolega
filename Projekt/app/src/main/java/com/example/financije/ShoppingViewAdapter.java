package com.example.financije;

import android.content.Context;
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
                Toast.makeText(nContext, produkt.get(position).getName() + " selected.", Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    public int getItemCount() {
        return produkt.size();
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
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            parent = itemView.findViewById(R.id.parent);
            imgShop = itemView.findViewById(R.id.imgShop);
            txtIme = itemView.findViewById(R.id.textProdukt);
            txtCijena = itemView.findViewById(R.id.textcijena);


        }
    }
}
